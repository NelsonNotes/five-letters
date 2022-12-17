import React, { useEffect, useState } from 'react'

import './Game.css'

import { useAppDispatch } from '../../hooks/app'
import { userOperations } from '../../store/user/operations'
import { useSelector } from 'react-redux'
import { selectUser } from '../../store/user/selectors'
import { selectSession } from '../../store/session/selectors'
import { selectAttempt } from '../../store/attempt/selectors'
import { LogoutButton } from '../recycled/LogoutButton'
import { TAttemptResponse } from '../../types/attempt'
import { GameBoard } from './GameBoard'
import { MakeAttempt } from './MakeAttempt'

export const GamePage: React.FC = () => {
	const dispatch = useAppDispatch()

	const user = useSelector(selectUser)
	const session = useSelector(selectSession)
	const attempt = useSelector(selectAttempt)

	const [userAttempts, setUserAttempts] = useState<TAttemptResponse[]>([])

	useEffect(() => {
		if (session.data) dispatch(userOperations.fetch())
	}, [session])

	useEffect(() => {
		setUserAttempts(user.data?.attempts || [])
	}, [user])

	useEffect(() => {
		if (attempt.data && !attempt.loading && !attempt.error)
			setUserAttempts([...userAttempts, attempt.data])
	}, [attempt])

	return (
		<div>
			<GameBoard userAttempts={userAttempts} />
			<LogoutButton />
			<MakeAttempt />
		</div>
	)
}
